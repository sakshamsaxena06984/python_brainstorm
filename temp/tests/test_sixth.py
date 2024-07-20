# import pytest
# # from .helper import Helper  # Replace with actual module path
# from ..sixth import Helper
# from unittest.mock import patch
# # helper.py
#
# import unittest
# from unittest.mock import patch, MagicMock
#
# import unittest
# from unittest.mock import patch, MagicMock
#
# # Assuming Helper is defined in a separate module
# from your_module import Helper
#
# class TestHelper(unittest.TestCase):
#
#     @patch('your_module.catch', MagicMock())  # Mocking the 'catch' import
#     def test_sum(self):
#         helper = Helper()
#         result = helper.sum(10, 5)
#         self.assertEqual(result, 15)
#
#     @patch('your_module.catch', MagicMock())  # Mocking the 'catch' import
#     def test_min(self):
#         helper = Helper()
#         result = helper.min(10, 5)
#         self.assertEqual(result, 5)
#
# if __name__ == '__main__':
#     unittest.main()

from abc import ABC, abstractmethod

class DataprocAbstraction(ABC):
    def __init__(self,
                 s_d: dict,
                 a_m_s:dict,
                 c_c: dict,
                 t_c: dict,
                 p_n: str,
                 u_c_p_r: str) -> None:
        self.s_d = s_d
        self.a_m_s = a_m_s
        self.c_c = c_c
        self.t_c = t_c
        self.p_n = p_n
        self.u_c_p_r = u_c_p_r

    @abstractmethod
    def get_submit_job_config(self)-> dict:
        pass

    def get_input_output_model_file_path(self)-> [str, str, str]:
        framework = self.s_d['framework']
        input_path_ori = framework['inputFileLocation']
        input_path_var = input_path_ori.split('$')[1].split('/')[0]
        input_path_val = self.c_c[input_path_var]
        model_file_path = f"gs://{self.p_n}/{self.u_c_p_r}/tasks"
        return input_path_val, input_path_ori, model_file_path

    def get_spark_cluster_jars(self)-> list:
        spark_cluster_jars = [
            f"gs://{self.p_n}/aida_jar/aida-0.2.1-SNAPSHOT.jar"
        ]
        return spark_cluster_jars



from aida.providers.airflow.infra.lumi.operators.scoring.abstract import DataprocAbstractScoringConfig


class DataprocXGBoostConfig(DataprocAbstractScoringConfig):
    def get_submit_job_config(self)-> dict:
        xgboost_input = self.get_xgboost_params()
        xgboost_jar = self.get_xgboost_jar()
        spark_jars = self.get_spark_cluster_jars()
        spark_jars.append(f"all_jars={spark_jars}")
        spark_job = {
            "main_class":"com.expr.aida.scoring.xgboost.XgBoostSparkDriver",
            "jar_file_uris":spark_jars,
            "args":[xgboost_input]
        }
        return spark_job

    def get_xgboost_params(self) -> str:
        input_final, output_final, model_file_path = self.get_input_output_model_file_path()
        params = f"if={input_final},of={output_final},mf={model_file_path}"
        algorithm = self.scoring_descriptor['algorithm']

        if 'ntreeLimit' in algorithm:
            params = params + f",tl={algorithm['ntreeLimit']}"
        if 'predContribs' in algorithm:
            params = params + f",pc={algorithm['predContribs']}"
        return params

    def get_xgboost_jar(self)-> str:
        algo_version = self.aida_model_store.get('model_algorithm_version')
        if "0.9"==algo_version:
            return f"gs://{self.project_name}/aida_jars/xgboost4j-0.090"
        else:
            None


# ======
from datetime import datetime
from typing import Optional
def fun(dag_run_id:str)-> tuple:
    data_str=dag_run_id[dag_run_id.rfind("_")+1:]
    formatted = datetime.strptime(data_str[:data_str.find('T')+9], "%Y-%m-%d%H:%M:%S")
    ds = formatted.strptime("%F")
    ts = formatted.strptime("%Y%m%d%T%H%M%S")
    return ds, ts

def get_run_date(**context):
    run_id = context["run_id"].lower()
    if run_id.startswith("backdated") or run_id.startswith("triggered"):
        ds = context["dag_run"].conf["runDate"]
        ts = context["dag_run"].conf["runTimeStamp"]
    else:
        dag_ds, ts = ('2024-07-15', '20240715T143000')
        ds = context["dag_run"].start_date.strftime("%F")
    return ds,ts
