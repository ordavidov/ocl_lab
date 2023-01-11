FROM adoptopenjdk/openjdk11:latest

# Install wget

RUN apt-get update -y && apt-get install -y \
	wget \
  git \
  maven \
	build-essential \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*

ARG gplk_version=glpk-4.65

# Install glpk from http
# instructions and documentation for glpk: http://www.gnu.org/software/glpk/

WORKDIR /user/local/
RUN wget http://ftp.gnu.org/gnu/glpk/${gplk_version}.tar.gz \
	&& tar -zxvf ${gplk_version}.tar.gz  

WORKDIR /user/local/${gplk_version}
RUN ./configure \
	&& make \
	&& make check \
	&& make install \
	&& make distclean \
	&& ldconfig \
	&& rm -rf /user/local/${gplk_version}.tar.gz \
	&& apt-get clean

# Install camel

ARG camel_version=1.5.1

RUN wget https://github.com/apache/camel-k/releases/download/v1.5.1/camel-k-client-${camel_version}-linux-64bit.tar.gz \
    && tar zxvf camel-k-client-${camel_version}-linux-64bit.tar.gz \
    && cp ./kamel /usr/local/bin

# Install python

ARG python_version=3.8

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        # ca-certificates \
        # curl \
        python${python_version} \
        python3-pip \
        python3.8-dev \
        python3-setuptools \
        python3-wheel

RUN pip install \
  opticl \
  doframework \
  jupyter

# Fix cython warning

RUN pip install GPy==1.9.9

# Get lab

# RUN git clone https://github.com/ordavidov/ocl_lab.git /ocl_lab

WORKDIR /ocl
ADD notebooks notebooks

CMD jupyter notebook --no-browser --allow-root --ip 0.0.0.0 --port 8888 notebooks