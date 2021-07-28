FROM tensorflow/tensorflow:2.2.3

ARG jupyterlab_version=3.0.15

RUN mkdir workspace
RUN pip3 install wget jupyterlab==${jupyterlab_version}
RUN pip3 install -q tensorflow-recommenders

COPY ./files /workspace

EXPOSE 8888
WORKDIR /workspace
CMD jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token=