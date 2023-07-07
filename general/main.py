import asyncio
from converts import BaseSettings, ModelInfo, getListModelInfo
from logics import handle_labels, handle_model, handle_model_types, handle_model_groups
from utils import run_sequence, run_parallel
import time


async def insert_data(baseSettings: BaseSettings, model_info: ModelInfo):
    url_label = baseSettings.getLabelUrl()
    url_model = baseSettings.getModelUrl()
    url_model_type = baseSettings.getModelTypeUrl()
    url_model_group = baseSettings.getModelGroupUrl()

    token = 'Token ' + str(baseSettings.ADMIN_TOKEN)
    headers = {'Authorization': token}

    labels, shape_type_mappings = model_info.getLabelShapeMapping()
    model_name = model_info.getModelName()
    model_types = model_info.getModelTypes()
    gpu_usage = model_info.getGPUUsage()
    deploy_script = model_info.getDeployScript()

    model_types, model_groups = model_info.getModelTypeGroupMapping()
    origin_source_path = model_info.getOriginSourcePath()
    print("RUN", model_name)
    await run_sequence(
        handle_labels(url_label, headers, labels, shape_type_mappings),
        handle_model(url_label, url_model, headers, labels, 
                             shape_type_mappings, model_name, gpu_usage, deploy_script, origin_source_path),
        handle_model_types(url_model, url_model_type, 
                                 headers, model_name, model_types),
        handle_model_groups(url_model_type, url_model_group, 
                                 headers, model_types, model_groups)
    )




async def main():
    file_path = './general/configs.yaml'
    baseSettings, model_objs = getListModelInfo(file_path)

    begin = time.perf_counter()
    await run_parallel(*[insert_data(baseSettings, model_info) 
                  for model_info in model_objs])
    print("TOTAL TIME: ", time.perf_counter() - begin)


    # print(baseSettings)
    # model_types, model_groups = model_objs[0].getModelTypeGroupMapping()
    # print(model_types)
    # print(model_groups)
    # print(model_objs[0].getModelType())

if __name__ == '__main__':
    asyncio.run(main())
