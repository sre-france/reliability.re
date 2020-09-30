# Reliability Report 📰

A collaborative curated content site about Reliability Engineering.

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](code_of_conduct.md)

## Contributing

Thank you for your interest in collaborate to this project :tada:

There are 2 kind of contributions for this project:

1. If you want to share and publish content please follow [these instructions](content/contribute.md).
2. For other contributions, like fixing typos, Github's workflows or improving static content, please see [CONTRIBUTING.md](CONTRIBUTING.md).

## Code of conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## Dev & Build

If you want to test changes or build a local copy of this site you'll to install [Hugo](https://gohugo.io/getting-started/quick-start/), run:

```
$ git clone https://github.com/sre-paris/reliability.re.git
$ cd reliability.re
$ hugo -D server

                   | EN  
-------------------+-----
  Pages            | 16  
  Paginator pages  |  0  
  Non-page files   |  0  
  Static files     |  7  
  Processed images |  0  
  Aliases          |  0  
  Sitemaps         |  1  
  Cleaned          |  0  

Built in 33 ms
Watching for changes in reliability.re/{archetypes,content,layouts,static,themes}
Watching for config changes in reliability.re/config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```
and visit http://localhost:1313/ on your browser.
