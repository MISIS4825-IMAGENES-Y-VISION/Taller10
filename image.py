import modal

image = modal.Image.from_registry(
    "nvidia/cuda:13.2.1-devel-ubuntu24.04", add_python="3.14"
).uv_pip_install(
    "grain",
    "jax[cuda13]",
    "keras",
    "pillow",
    "pandas",
    "matplotlib",
    "ipykernel",
    "ipywidgets",
)

app = modal.App("Taller_10_IV")


@app.function(image=image)
def main():
    pass
