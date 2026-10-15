import os
import socket

from fastapi import FastAPI

VERSION = os.getenv("APP_VERSION", "v1")

app = FastAPI(title="FastAPI GitOps", version=VERSION)


@app.get("/")
def root():
    return {"message": "Hello from FastAPI GitOps", "version": VERSION}


@app.get("/version")
def version():
    """Shows which image version is running (demo 1: v1 -> v2)."""
    return {"version": VERSION}


@app.get("/info")
def info():
    """Shows which pod answered (demo 1: more replicas = different hostnames)."""
    return {"pod": socket.gethostname(), "version": VERSION}


@app.get("/health")
def health():
    """Used by the Kubernetes readiness and liveness probes."""
    return {"status": "ok"}
