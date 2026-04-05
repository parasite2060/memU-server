# Changelog

## [0.2.0](https://github.com/parasite2060/memU-server/compare/v0.1.0...v0.2.0) (2026-04-05)


### Features

* add clear and categories endpoints with tests ([#21](https://github.com/parasite2060/memU-server/issues/21)) ([ba1b16b](https://github.com/parasite2060/memU-server/commit/ba1b16bb2fccb2771ecd1d289cf37e95f14e53ba))
* add database migration support and connection utilities ([#17](https://github.com/parasite2060/memU-server/issues/17)) ([258439c](https://github.com/parasite2060/memU-server/commit/258439cb5ec9aacb5cece82e901d5ddbf4a34449))
* add issue templates with verified signature ([#7](https://github.com/parasite2060/memU-server/issues/7)) ([32bf4f4](https://github.com/parasite2060/memU-server/commit/32bf4f414040b464c683b24e241bb568278ad07e))
* add Temporal worker integration with memorize workflow and tests ([#22](https://github.com/parasite2060/memU-server/issues/22)) ([0002c21](https://github.com/parasite2060/memU-server/commit/0002c21cb2f4f0736794aa3b205b3c919a3fd356))
* async memorize via Temporal + task status endpoint ([#23](https://github.com/parasite2060/memU-server/issues/23)) ([d325329](https://github.com/parasite2060/memU-server/commit/d3253297f2502196266eedadaababe9f003a0529))
* initialize simple fastapi server for memU ([#1](https://github.com/parasite2060/memU-server/issues/1)) ([9f9cd74](https://github.com/parasite2060/memU-server/commit/9f9cd74893af372f43b45b2599664de904bc45bc))
* initialize with AGPL license ([495d280](https://github.com/parasite2060/memU-server/commit/495d28056aca159044de48ae197450ef09c9032e))


### Bug Fixes

* Azure OpenAI compatibility and add gunicorn dependency ([02d7f2e](https://github.com/parasite2060/memU-server/commit/02d7f2e875f968423e1a8e9dd270dd43a4ce90b9))
* **ci:** use memu-wheel directory with gitkeep for Docker wheel install ([d3d92ee](https://github.com/parasite2060/memU-server/commit/d3d92eebac3316e86978ab5fe71b8f568db6bdca))
* **ci:** use uv pip install instead of .venv/bin/pip ([e2d3851](https://github.com/parasite2060/memU-server/commit/e2d38517ca3c03e5a701d966d144585ea2d28a98))
* install git in Docker image for git+https dependency ([e246da2](https://github.com/parasite2060/memU-server/commit/e246da27a1f26dbedf135bbcdaf221ba867b06cb))
* remove unnecessary entrypoint in Dockerfile ([#4](https://github.com/parasite2060/memU-server/issues/4)) ([a3818a0](https://github.com/parasite2060/memU-server/commit/a3818a072accbc2aa24a47df8dda5b18cf76aafb))
* use PyPI memu-py with file-level Azure OpenAI patches ([bff39d9](https://github.com/parasite2060/memU-server/commit/bff39d9cc962ddecb5a2780c49d76d1431b6381a))
* use venv python to locate memu-py install path ([c0b9688](https://github.com/parasite2060/memU-server/commit/c0b96883a14fff0ef106dffa9db186308bf35785))


### Documentation

* add Get Started section to README.md ([#3](https://github.com/parasite2060/memU-server/issues/3)) ([77a0ab2](https://github.com/parasite2060/memU-server/commit/77a0ab2b45bc596bde58c0f3939185031e838283))
* add README description ([#2](https://github.com/parasite2060/memU-server/issues/2)) ([de8635b](https://github.com/parasite2060/memU-server/commit/de8635b35ed4366baffdd111361200b42d52eec4))
* update README with current architecture, API reference, and deployment guide ([#24](https://github.com/parasite2060/memU-server/issues/24)) ([1707171](https://github.com/parasite2060/memU-server/commit/170717163fcd19e5bcb55d8139999f7e7d28dc52))
