# import pendu lum
import pendulum

# timezone = pendulum.tz.timezone('UTC')
# print(timezone)

timezone = pendulum.timezone('UTC')
print(timezone)

print(pendulum.local_timezone())
# print(pendulum.)
# def get_context_info(context):
#     run_id = context['run_id']
#     run_date = context['ds']
#     dag_name = context['dag'].dag_id
#     dag_run_status = context['dag_run'].state

def help(task_group_id: str, default_task_id: str, **context) -> str:
    tis_dagrun = context["ti"].get_dagrun().get_task_instances()
    for general_task in tis_dagrun:
        if task_group_id in general_task.task_id and general_task.state == "FAILED":
            return f"user_pipeline.{task_group_id}.{default_task_id}"
from datetime import datetime

def handle_branch (taskgroup_dict, task_group_id):
    for x in taskgroup_dict:
        if x["task_group_id"] == task_group_id:
            each_taskgroup_dict=x
    op_task = None

    if(
        len(each_taskgroup_dict["branch"])==1
        and "condition" not in each_taskgroup_dict["branch"][0]
    ):
        op_task = each_taskgroup_dict["branch"][0]
    else:
        for each in each_taskgroup_dict["branch"]:
            data_cond = each["condition"]
            val = data_cond.split("[", 1)[1].split("]")[0]
            bw_list = [val.split(",")[0], val.split(",")[1]]
            now=datetime.today()
            if(
                datetime.strptime(str(bw_list[0]).strip(), "%Y-%m-%d")
                < now
                < datetime.strptime(str(bw_list[1]).strip(), "%Y-%m-%d")
            ) or (
                datetime.strptime(str(bw_list[0]).strip(), "%Y-%m-%d")
                > now
                > datetime.strptime(str(bw_list[1]).strip(), "%Y-%m-%d")

            ):
                op_task = each["task_id"]
                break
    if op_task is None and "default" in each_taskgroup_dict.keys():
        raise Exception("No valid data")
    return f"user_pipeline.{each_taskgroup_dict['task_group_id']}.{op_task}"


def get_context_info(context):
    run_id=context['run_id']
    run_date=context['ds']
    dag_name=context['dag'].dag_id
    dag_run_status = context['dag_run'].state
    return run_id, run_date, dag_name, dag_run_status

# class TaskGroupDefaultLogic()

def send_task_group_default_email(pipeline_id:int, pipeline_version:int, env:str,
                                  run_type: str, task_name:str, **context):
    run_id, run_date, dag_name, dag_run_status = get_context_info(context)

