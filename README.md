# learn_devops_data_engg
(wip) Notes on learnings from model deployment, REST API setup and tools

This covers the live scenario. The batch prediction mode is well explored.

[ ] Create REST API for a scikit-learn model. Options: [flask](https://towardsdatascience.com/deploying-models-to-flask-fb62155ca2c4), [openscoring](openscoring) (with pmml), ngnix

[ ] Deploy using kubernetes / docker. Explore kubeflow.

[ ] Deploy the kubernetes on a cloud server (Options: AWS, azure). How does a kubernetes cluster play with this?

[ ] Learn how to live update the model without stopping the service

[ ] Package the four steps above for quick deployment

----

[ ] Extend the above for a tensorflow model. Options: [tensorflow serve](https://www.tensorflow.org/tfx/tutorials/serving/rest_simple)

[ ] Extend the above for spark models. Options: [mleap](https://mleap-docs.combust.ml/), [mlflow](https://mlflow.org/docs/latest/models.html)
