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



 # ----

from aida.providers.airflow.infra.lumi.operators.scoring.abstract import DataprocAbstraction

class DataprocUGBoostConfig(DataprocAbstraction):

    def get_submit_job_config(self) -> dict:
        ugboost_input = self.get_ugboost_params()
        spark_job = {
            "main_class ":"com.aida.UgBoostPrediction",
            "args": [ugboost_input]
        }
        return  spark_job

    def get_ugboost_params(self)-> str:
        framework = self.scoring_descriptor['framework']
        algorithm = self.scoring_descriptor['algorithm']
        input_path_ori = framework['inputFileLocation']
        input_path_var = input_path_ori.split('$')[1].split('/')[0]
        input_path_val = self.c_c[input_path_var]
        input_final = input_path_ori.replace(f"${input_path_var}",input_path_val)
        output_path_ori = framework['outputFileLocation']
        output_path_var = output_path_ori.split('$')[1].split('/')[0]
        output_path_val = self.c_c[output_path_var]
        output_final = output_path_ori.replace(f"${output_path_var}",output_path_val)
        params = f"input={input_final},output={output_final}"
