# coding: utf-8
# 実行ファイル
import sys
import func

args = sys.argv


googlePlayURL = "https://play.google.com/store/apps/details?id=com.hoge.hoge&hl=ja"
funcs = func.Functions(googlePlayURL)
#funcs = funcs.Functions(args[1])
funcs.get_all()