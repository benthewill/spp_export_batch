import os
import sys
# Substance 3D Painter modules
import substance_painter.ui
import substance_painter.export
import substance_painter.project
import substance_painter.resource
import substance_painter.textureset
import substance_painter.display
import substance_painter_plugins

# Change work_dir to the folder with your .spp files
work_dir = r"C:\Users\berna\OneDrive\Documents\test_export"

# Change the export preset name accordingly. If it's a built-in preset, use "starter_assets" for the context. Otherwise, use "your_assets"
export_preset_name = "UE5"
export_preset_context = "your_assets"


def all_export_presets():
    starter_export_presets = os.listdir(sys.path[0] + r"\resources\starter_assets\export-presets")
    starter_export_presets_list = []

    for file in starter_export_presets:
        if file.endswith('.spexp'):
            starter_export_presets_list.append(file[0:-6])

    my_asset_export_presets = os.listdir(
        substance_painter_plugins.path[0].replace('/python', '') + r"\assets\export-presets")
    my_asset_export_presets_list = []

    for file in my_asset_export_presets:
        if file.endswith('.spexp'):
            my_asset_export_presets_list.append(file[0:-6])

    all_export_presets_list = starter_export_presets_list + my_asset_export_presets_list
    # print(f'TOTAL COMBINED: {len(all_export_presets_list)}')
    # print(all_export_presets_list)
    formatted_starter_export_presets = []

    for x in starter_export_presets_list:
        formatted_starter_export_presets.append({
            "context": "starter_assets",
            "name": x
        })

    for x in my_asset_export_presets_list:
        formatted_starter_export_presets.append({
            "context": "starter_assets",
            "name": x
        })

    return {
        "starter_assets": starter_export_presets_list,
        "your_assets": my_asset_export_presets_list,
        "combined": all_export_presets_list,
        "formatted": formatted_starter_export_presets
    }


def start_plugin():
    work_dir_list = os.listdir(work_dir)
    all_projects = []
    for x in work_dir_list:
        if x.endswith('.spp'):
            all_projects.append(x)

    print(all_projects)

    for project in all_projects:
        if substance_painter.project.is_open():
            substance_painter.project.close()
        current_project = work_dir + '\\' + project
        current_project_name = project.replace('.spp', '')

        substance_painter.project.open(current_project)

        export_preset = substance_painter.resource.ResourceID(
            context=export_preset_context, name=export_preset_name)

        all_texture_sets = []
        for texture_set in substance_painter.textureset.all_texture_sets():
            all_texture_sets.append({
                "rootPath": texture_set.name()
            })

        export_path = os.path.join(work_dir, 'exports', current_project_name)
        if not os.path.exists(export_path):
            os.makedirs(export_path)

        export_config = {
            "exportShaderParams": False,
            "exportPath": export_path,
            "defaultExportPreset": export_preset.url(),
            "exportList": all_texture_sets,
            "exportParameters": [
                {
                    "parameters": {
                        "fileFormat": "png",
                        "bitDepth": "8",
                        "dithering": True,
                        "paddingAlgorithm": "infinite"
                    }
                }]
        }

        export_result = substance_painter.export.export_project_textures(export_config)

        if export_result.status != substance_painter.export.ExportStatus.Success:
            print(export_result.message)

            # Display the details of what was exported:
        for k, v in export_result.textures.items():
            print("Stack {0}:".format(k))
            for exported in v:
                print(exported)

        substance_painter.project.close()


def close_plugin():
    # Remove all widgets that have been added to the UI
    print("closed")


if __name__ == "__main__":
    start_plugin()
