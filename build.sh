#!/bin/bash -ex

echo "Phase 1: Generate the thrift WeltamDraht API"
thrift -r --gen py weltamdraht.thrift
thrift -r --gen py:twisted weltamdraht.thrift

echo "Phase 2: Create the Python WeltamDraht API package."
rm -fr package/weltamdraht
mkdir -p package/weltamdraht/tx
cp -fr gen-py/weltamdraht/*.py package/weltamdraht
cp -fr gen-py.twisted/weltamdraht/*.py package/weltamdraht/tx

