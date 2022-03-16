#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/15 14:12
# @Author  : Rocky
# @Site    : 
# @File    : base64.py
# @Software: PyCharm

import base64
import json
import os

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models
import pandas as pd






params = {

}
def test():
    path = "img/Part2_212.jpg"
    fout = open("out/x.txt", 'wb')
    with open(path, "rb") as fin:
        text = base64.b64encode(fin.read())
        print(text)
        fout.write(text)

    fout.close()


def list_split(items, n):
    return [items[i:i + n] for i in range(0, len(items), n)]


def parse_image():
    secretId = "AKIDSkmZ6NNDm44nEOHtFK7dtrYz93g27vSh"
    secretKey = "ziAMHuHNjpfDUUDfqkMinb8RYQ1PXOyH"
    try:
        cred = credential.Credential(secretId, secretKey)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile)

        req = models.RecognizeTableOCRRequest()

        # params = {"ImageBase64": ''}
        # fout = open("b.txt", 'wb')
        # path = "Part1_72.jpg"
        req.from_json_string(json.dumps(params))
        resp = client.RecognizeTableOCR(req)
        list = []
        cells = json.loads(resp.to_json_string())['TableDetections'][0]['Cells']

        dict_tmp= {}
        for v in cells:
            dict_tmp[v['RowBr']] = []

        for v in cells:
            dict_tmp[v['RowBr']] = dict_tmp.get(v['RowBr']) + [v['Text']]

        df = pd.DataFrame(dict_tmp.values())
        df.to_excel("guiyang212.xlsx", index=False)

    except TencentCloudSDKException as err:
        print(err)


if __name__ == '__main__':
    # parse_image()
    test()