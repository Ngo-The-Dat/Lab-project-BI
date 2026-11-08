FROM mageai/mageai:latest

ARG USER_CODE_PATH=/home/src

# Cai dat them cac package Python can cho do an
COPY docker/requirements.txt ${USER_CODE_PATH}/requirements.txt
RUN pip3 install --no-cache-dir -r ${USER_CODE_PATH}/requirements.txt

