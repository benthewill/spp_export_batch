# Substance Painter - Batch Exporter

Substance Painter - Batch Exporter is a plugin for Adobe Substance Painter 3D for exporting multiple `*.spp` files within a specified folder.

## Installation
#### This plug-in is currently only available on Windows.
1. Download the `export_batch.py` file.
2. Copy the python file into your Adobe Substance 3D Painter's python plugins folder. 
   - It is usually located at `Users\<your_username>\Documents\Adobe\Adobe Substance 3D Painter\python\plugins`
   - If you can't find it, open Substance Painter and select the _Python_ menu in the toolbar and click the _Plugins Folder_.
3. Open the `export_batch.py` file with your preferred Text Editor/IDE.
4. Change the `work_dir` variable to the directory where your `*.spp` files live.
5. Change the export preset name and context accordingly. If it's a built-in preset, use `"starter_assets"` for the context. Otherwise, use `"your_assets"`
5. Open Substance Painter.
6. The plugin `export_batch` should be listed in the _Python_ menu. If not, select the _Reload Plugins Folder_.
7. Run the plugin.
8. Your textures should be inside the `<work_dir>\exports` folder. 

## Known Issues
- If there's an error during runtime and the plugin is unable to perform the export function due to insufficient information, Substance Painter might crash. This is very rare; However, if this happens, when re-opening Substance Painter, you might get stuck at the **Loading Scene** panel. To fix the program:
    1. End Substance Painter using Task Manager
    2. Delete / move the `export_batch.py` file somewhere else temporarily.
    3. Run Substance Painter
    4. Move the `export_batch.py` back to the plugins folder
    5. Re-run the plugin