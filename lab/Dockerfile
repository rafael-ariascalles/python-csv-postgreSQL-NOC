FROM tensorflow/tensorflow:2.2.3

ARG spark_version=3.0.0
ARG jupyterlab_version=3.0.15

RUN mkdir workspace
RUN pip3 install wget jupyterlab==${jupyterlab_version}
 
COPY ./files /workspace

EXPOSE 8888
WORKDIR /workspace
CMD jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token=