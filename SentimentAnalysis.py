#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 12:09:23 2022

@author: magnusaxen
"""
SampleText="BEAVERTON, Ore.--(BUSINESS WIRE)--Earlier in September, a virtual meeting was organised by the Media Coding Industry Forum (MC-IF) to encourage fostering of a licensing programme of patents essential to the VVC standard. Forty-five companies were present at the meeting, including BBC, Bytedance, b<>com, Canon Inc., Enghouse Vidyo, Ericsson, ETRI, FG Innovation, Hikvision, Huawei, Ideahub, Intel, Intellectual Discovery, InterDigital, JVCKENWOOD, Kuaishou, Maxell, Mitsubishi Electric, NHK, NTT Corporation, NTT DOCOMO, OPPO, Panasonic, Siemens AG, Sony, and Tencent. These companies are from different countries, and represent different industries and business models. Each has a well-founded belief that it holds patents essential to the Versatile Video Coding standard (VVC, ISO/IEC 23090-3 | ITU-T Recommendation H.266).During the meeting, the participants agreed that their objective is selection, if possible by consensus of participants, of an administrator to facilitate the formation of a single patent licensing pool covering a critical mass of patents essential to the VVC standard. They are developing a schedule for presentations of proposals from candidate administrators."


SampleText=SampleText.lower()
SampleText = SampleText.encode("ascii", "ignore")
string_decode = SampleText.decode()