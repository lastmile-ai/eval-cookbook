# LastMile AI RAG-Debugger Cookbook
The RAG-Debugger Cookbook is a companion repository to the RAG-Debugger, providing a collection of tutorials and recipes to help you effectively evaluate and debug your RAG applications. This repository offers a comprehensive guide for setting up tracing, evaluations metrics, test sets, and more to help you easily diagnoise and improve your RAG applications. 

## Table of Contents
### `quickstart/`

| Recipe | Description |
|---|---|
[getting_started](https://github.com/lastmile-ai/eval-cookbook/blob/main/quickstart/getting_started.ipynb) | Start here if you are new to using the RAG-Debugger. This notebook is the "Hello World" of using RAG-Debugger.


### `examples/`

Contains example scripts focused on a particular topic:  
| Recipe | Description |
|---|---|
evaluation_metrics  [TODO Add link] | Script to setup evaluation metrics (generic and RAG-specific metrics)
[tracing_setup](https://github.com/lastmile-ai/eval-cookbook/blob/main/examples/Tracing%20Setup.ipynb) | Script to setup tracing and logging for your RAG application
[test_set_creation](https://github.com/lastmile-ai/eval-cookbook/blob/main/examples/Test%20Set%20Creation%20Setup.ipynb) | Script to setup and manage test sets (aka datasets) to evaluate your RAG system
[distributed_tracing](https://github.com/lastmile-ai/eval-cookbook/blob/main/examples/Distributed%20Tracing.ipynb) | Script to setup distributed tracing which allows you to track and analyze the flow of requests across multiple services or components in a distributed system. 
[online_feedback](https://github.com/lastmile-ai/eval-cookbook/blob/main/examples/Online%20Feedback%20Setup.ipynb) | Script to setup logging online feedback (ex. thumbs up/down for users) to help debug your RAG system

### `deprecated_examples/`
Over time, certain tutorials may become outdated or no longer relevant due to updates in the RAG-Debugger. These deprecated tutorials are moved to the deprecated_recipes folder to maintain the clarity and relevance of the main tutorial section.

* [deprecated_examples/](https://github.com/lastmile-ai/eval-cookbook/tree/main/deprecated_examples/cohere_ai)

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## Feedback or Questions

If you have any questions, suggestions, or encounter any issues while using the RAG Debugger or following the tutorials, please don't hesitate to reach out to us [Discord](https://discord.com/invite/xBhNKTetGx).

We're here to assist you in your evaluation journey and ensure that you get the most out of the RAG-Debugger.

Happy debugging! 