# from __future__ import annotations
# from typing import Any, Callable
# import requests
# from requests_toolbelt.adapters.socket_options import TCPKeepAliveAdapter
# from airflow.providers.http.hooks.http import HttpHook
#
# class AidaHttpHook(HttpHook):
#     conn_name_attr = "http_conn_id"
#     default_conn_name = "http_default"
#     conn_type = "http"
#     hook_name = "HTTP"
#
#     def __init__(self,
#                  method: str = "POST",
#                  http_conn_id: str = default_conn_name,
#                  auth_type: Any = None,
#                  tcp_keep_alive: bool = True,
#                  tcp_keep_alive_idle: int = 120,
#                  tcp_keep_alive_count: int = 20,
#                  tcp_keep_alive_interval: int = 30,
#                  ) -> None:
#                     self.http_conn_id= http_conn_id,
#                     self.method = method.upper()
#                     self.base_url: str=""
#                     self._retry_obj: Callable[..., Any]
#                     self._auth_type: Any = auth_type
#                     self.tcp_keep_alive = tcp_keep_alive
#                     self.keep_alive_idel = tcp_keep_alive_idle
#                     self.keep_alive_count = tcp_keep_alive_count
#                     self.keep_alive_interval = tcp_keep_alive_interval
#
#     def run(self,
#             endpoint: str | None = None,
#             data: dict[str, Any] | str | None = None,
#             headers: dict[str, Any] | None = None,
#             extra_options: dict[str, Any] | None = None,
#             **request_kwargs: Any
#             ) -> Any:
#         extra_options = self.get_conn(headers)
#         session = self.get_conn(headers)
#         url = self.url_from_endpoint(endpoint)
#         if self.tcp_keep_alive:
#             keep_alive_adapter: TCPKeepAliveAdapter(
#                 idle=self.keep_alive_idle,
#                 count=self.kepp_alive_count,
#                 interval=self.keep_alive_interval,
#             )
#             session.mount(url, keep_alive_adapter)
#         if self.method == "GET":
#             req = requests.Request(
#                 self.method, url, params=data, headers=headers, **request_kwargs
#             )
#         elif self.method == "HEAD":
#             req = requests.Request(
#                 self.method, url, json=data, headers=headers, **request_kwargs
#             )
#         else:
#             req = requests.Request(
#                 self.method, url, json=data, headers=headers, **request_kwargs
#             )
#         preppend_request = session.prepare_request(req)
#         return self.run_and_check(session, preppend_request, extra_options)
#
#
# @classmethod
# def get_connection_from_secrets(cls, conn_id: str) -> Connection:
#     for secrets_backend in ensure_secrets_loaded():
#         try:
#             conn = secrets_backend.get_connection(conn_id=conn_id)
#             if conn:
#                 return  conn
#         except Exception as err:
#             print(err)
#
#     raise AirflowNotFoundException(f"The conn_id `{conn_id}` is not defined")
#
#
# class AirflowCSLogs(HiveLogs, SparkLogs, AirflowLogs):
#     def __init__(self, **kwargs):
#         context = kwargs["context"]
#
#     def get_airflow_log(self, task_id: str )-> str:
#         pass
#


import tarfile
import os
from aida.providers.airflow.models.model_artefact_download_operator import ModelArtefactDownloadOperator as Abstract
# from aida.providers.airflow.infra.cs.uils import download
  #---------


# import requests
# def download_file(url, local_filename):
#     with requests.get(url, stream=True, verify=False) as r:
#         r.raise_for_status()
#         with open(local_filename,"wb") as f:
#             for chunk in r.iter_content(chunk_size=8192):
#                 f.write(chunk)
#     return local_filename
#
#
# import tarfile
# import os
# from aida.providers.airflow.models.model_artefact_download_operator import ModelArtefactDownloadOperator as Abstract
# class ModelArtefactDownloadOperator(Abstract):
#     def decide_download_model_artefects(self, model_file_name:str , source_code_path: str) -> bool:
#         path = f"{source_code_path}/task/task4_scoring/model_artefects"
#         need_download = True
#         if model_file_name is not None and len(model_file_name)>0:
#             if os.path.exists(os.path.join(path, model_file_name)):
#                 need_download = False
#         else:
#             for (dir_path, dir_name, file_name) in os.walk(path):
#                 for file in file_name:
#                     split_tup = os.path.splitext(file)
#                     if split_tup[len(split_tup)-1] in self.allow_extension:
#                         need_download = False
#                         break
#         return need_download
#
#     def download_model_artefact(self, meta_data:dict, download_dir: str)-> None:
#         file_name = meta_data['fileName']
#         url = meta_data['url']
#         try:
#             original_umask = os.umask(0)
#             if not os.path.exists(download_dir):
#                 os.makedirs(download_dir, mode=0o777)
#             path = download_dir(url, f"{download_dir}/{file_name}")
#
#             if file_name.endswith('.gz') or file_name.endswith('.tar'):
#                 file = tarfile.open(path)
#                 file.extractall(download_dir)
#                 file.close()
#                 os.remove(path)
#             for root, d_names, f_names in os.walk(download_dir):
#                 for d in d_names:
#                     try:
#                         os.chmod(os.path.join(root, d), 0o777)
#
#                     except PermissionError:
#                         print("error")
#                     else:
#                         print("error1")
#                 for f in f_names:
#                     try:
#                         os.chmod(os.path.join(root,f),0o77)
#                     except PermissionError:
#                         print("errorv")
#
#                     else:
#                         print("errorv1")
#         finally:
#             os.umask(original_umask)

 #--------

# import pandas as pd
#
# def apply_filtration_logic(df: pd.DataFrame, filtration_threshold):
#     val_gini_threshold = filtration_threshold.get('val_gini_threshold')
#     val_accuracy_threshold = filtration_threshold.get('val_accuracy_threshold')
#     test_accuracy_threshold = filtration_threshold.get('test_accuracy_threshold')
#     gini_drop_threshold = filtration_threshold.get('gini_drop_threshold')
#
#     if val_gini_threshold is not None:
#         df = df[(df['eval_gini']>val_gini_threshold)]
#     if val_accuracy_threshold is not None:
#         df = df[(df['eval_accuracy']>val_accuracy_threshold)]
#     if test_accuracy_threshold is not None:
#         df = df[(df['test_accuracy']>test_accuracy_threshold)]
#     if gini_drop_threshold is not None:
#         df = df[(df['drop_in_gini']<gini_drop_threshold)]
#
#     return df
#
#
#
# def get_hpt_best_params(experiment_results_file:str, output_path:str, configs:dict, **context):
#     evaluation_threshold = pd.read_csv(experiment_results_file)
#
#     filtration_thresshold = configs.get("filtration")
#     if filtration_thresshold:
#         filtered_output_path = os.path.join(output_path, "filtered_hpt_results.csv")
#         evalution_results_df = ap
#
#
# class AttributesSection:
#     COMMON = "common"
#     CLUSTER_NAME = "cluster_name"


 # ------------
from typing import Sequence
from airflow.models.baseoperator import BaseOperator
from airflow.exceptions import AirflowFailException
from aida.providers.airflow.infra.lumi.utils import fs

def get_blob(filepath):
    bucket, object_name = _get_bucket(filepath)
    return bucket.blob(object_name)

def read_text_file(filepath: str):
    blob = get_blob(filepath)
    return blob.download_as_text(encoding="utf-8")
class ARVolum(BaseOperator):
    template_fields: Sequence[str] = {"pipeline_id","pipeline_version","env","file_path"}
    ui_color = "#ccff66"

    def __init__(self, file_path, pipeline_id, pipeline_version, env, run_type, **kwarge)->None:
        super(ARVolum, self).__init__(**kwarge)
        self.file_path = file_path
        self.pipeline_id = pipeline_id
        self.pipeline_version = pipeline_version
        self.env = env
        self.run_type = run_type

    def execute(self, context) -> str:
        val = (fs.read_text_file(filepath=self.file_path).lower().lstrip()).rstrip()

        if val !="true":
            context["ti"].xcom_push(key="STOP_AR_PIPELINE", value="VOLUME_SUFFICIENCY_FAIL")
            raise AirflowFailException('pipeline needs to stopped')
        return
