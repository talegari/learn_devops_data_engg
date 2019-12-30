# Notes on devops, data engineering and microservices

(wip) Notes on learnings from model deployment, REST API setup, microservices and tools. This mostly covers the live scenario. The batch prediction mode is well explored.

 - [x] Create REST API for a scikit-learn model. Options: [flask](https://towardsdatascience.com/deploying-models-to-flask-fb62155ca2c4), [openscoring](openscoring) (with pmml), ngnix
- [x] Deploy using kubernetes / docker. Explore kubeflow.
- [x] Deploy the kubernetes on a cloud server (Options: AWS, azure). How does a kubernetes cluster play with this?
- Learn how to live update the model without stopping the service
    - [ ] Mleap
    - [ ] openscoring
- Package the four steps above for quick deployment
    - [ ] Mleap
    - [ ] openscoring

----
- [ ] Extend the abobe for R models. Options: [restrserve](https://github.com/rexyai/RestRserve), [plumber](https://www.rplumber.io/), [opencpu](https://www.opencpu.org/)
- [ ] Extend the above for a tensorflow model. Options: [tensorflow serve](https://www.tensorflow.org/tfx/tutorials/serving/rest_simple)
- [ ] Extend the above for spark models. Options: [mleap](https://mleap-docs.combust.ml/), [mlflow](https://mlflow.org/docs/latest/models.html)

----
## Good reads
- [microservices and Datascience](https://mapr.com/blog/top-technology-trends-machine-learning-event-driven-microservices-dataops-and-cloud-to-edge/)
