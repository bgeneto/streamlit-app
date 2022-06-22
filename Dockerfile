# --------------
#  INSTRUCTIONS
#---------------
# Firts build the streamlit-base image and upload to your local registry
# using the build script provided in the streamlit-base directory/repo
# then simply edit your .env file and call docker compose up

FROM python:3-slim
COPY --from=localhost:5000/streamlit/streamlit-base:latest /root/.local /root/.local
WORKDIR app
COPY . .
EXPOSE 8501
ENV PATH=/root/.local/bin:$PATH
ENTRYPOINT ["streamlit", "run"]
CMD ["main.py"]
