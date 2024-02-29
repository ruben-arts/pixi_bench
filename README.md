# Automated benchmark for `pixi` `micromamba` `conda`

We use the awesome [`hyperfine`](https://github.com/sharkdp/hyperfine) library to compare runs.

Try it out:
```
pixi run start
```

Info on the tested tools
- [`pixi`](): Conda/PyPI package manager written in Rust, with batteries included like `tasks` `global virtual environments` and `multiple in-project environments`
-  [`micromamba`]: Conda virtual environment package manager written in C++. 
-  [`conda`]: The original Conda virtual environment package manager which was recently updated to use the C++ Mamba solver.


This benchmark uses the `mamba_env.yml` as input for the environment creation. Because `pixi` can't directly use an env.yml as a project source it uses `pixi init --import env.yml` to first convert it to a `pixi.toml` and then install that. Check the results in the `pixi/pixi.toml` after running the task.

