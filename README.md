# Cap3D_USD
Generate descriptions for USD models (e.g. Behaviour-1K) using Cap3D models.

## Decrypt the USD model of Behaviour-1K

(1) revise `objects_path` to objects path.

(2) run script.
```python
python decrypt.py
```



## Rendering images of Behaviour-1K model
(1) Replace the [`render_script.py`](https://github.com/crockwell/Cap3D/blob/afa247d407dadca3a69fdec345db27018a1fa9db/captioning_pipeline/render_script.py) in the [`Cap3D` project](https://github.com/crockwell/Cap3D) with the `render_script.py` of this project.

(2) Refer to [`Cap3D` project](https://github.com/crockwell/Cap3D) for the running steps.
