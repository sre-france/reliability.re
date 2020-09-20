# Reliability Report 📰

A collaborative curated content site about Reliability Engineering.

## Contribute

Thank you for your interest in collaborate to this project :tada:

If you want to share and publish content please follow [these instructions](content/contribute.md). 

For other contributions, like fixing typos, Github's workflows or improving static content, please open a [blank issue](https://github.com/sre-paris/reliability.re/issues/new) or fork this repository and create a PR.

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
