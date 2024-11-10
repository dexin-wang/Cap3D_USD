# Cap3D_USD
Generate descriptions for USD models (e.g. Behaviour-1K) using Cap3D models.

## Decrypt the USD model of Behaviour-1K

(1) revise `objects_path` to objects path.

(2) run script.
```python
python decrypt.py
```



## Rendering images of Behaviour-1K model
(1) clone [`Cap3D` project](https://github.com/crockwell/Cap3D) to pc

(2) write usd models path to `behaviour_1k/usd_object_path.pkl`
  - download `behaviour_caption.py` to `/home/.../Cap3D/captioning_pipeline/`
  - revise `behaviour_objects_path` in `behaviour_caption.py`
  - run cmd: `python behaviour_caption.py`

(3) run rendering
I found that the exposure of the rendered image would become stronger as the number of renderings increased, so I only rendered 50 objects each time I ran the program, and then re-ran the program to render the next 50.
  - download `render_every_50.py` to `/home/.../Cap3D/captioning_pipeline/`
  - Replace the [`render_script.py`](https://github.com/crockwell/Cap3D/blob/afa247d407dadca3a69fdec345db27018a1fa9db/captioning_pipeline/render_script.py) in the [`Cap3D` project](https://github.com/crockwell/Cap3D) with the `render_script.py` of this project.
  - Refer to [`Cap3D` project](https://github.com/crockwell/Cap3D) for install Blender
  - run cmd: `python render_every_50.py`
imgs would be saved in `/home/.../Cap3D/captioning_pipeline/behaviour_1k/Cap3D_imgs/Cap3D_imgs_view*`.
