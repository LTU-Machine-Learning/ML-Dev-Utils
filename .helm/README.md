# ML-Dev Python Template / Helm

Project folder structure needs to be:

```bash
ML-Dev-Utils/repository
ML-Dev-Utils/vscode-server
```

Clone repository into: ML-Dev-Utils/repository

```bash
cd ML-Dev-Utils/repository
git clone git@github.com:LTU-Machine-Learning/ML-Dev-Utils.git .
```

## Deploy on localhost

Check parameters in: `./.helm/values_local.yaml`

You need to set ENV for you local prject folder, for example:

```bash
export ML_DEV_UTILS_VOLUME_PATH=/.../ML-Dev-Utils
```

Deploy with the helper script. If you want to use helm commands instead, have a
look into the script.

```bash
./.helm/local_dev.sh start

./.helm/local_dev.sh stop

./.helm/local_dev.sh build
```

## Deploy on RISE ICE Kube

Check parameters in: `./.helm/values_icekube.yaml`

Deploy with the helper script. If you want to use helm commands instead, have a
look into the script.

```bash
./.helm/icekube_dev.sh start

./.helm/icekube_dev.sh stop

./.helm/icekube_dev.sh build
```

On first attachment you need to clone the repo inside the container:

```bash
# clone into the workspace folder
git init -b main
git remote add origin git@github.com:LTU-Machine-Learning/ML-Dev-Utils.git
git fetch
git checkout -t origin/main

# reload windows with command 'Developer: Reload Window' for checked out vsc settings
# probably reload window after extension installation

# The persistence volume will not be delete by helm.
# If you want to delete the volume, you need to do it explicit. All you data
# in the volume will be delete. Make sure to backup via rclone before!
kubectl delete pvc/...
```
