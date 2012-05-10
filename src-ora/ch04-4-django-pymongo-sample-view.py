
import datetime
import string
import random
import mimetypes
import cStringIO as StringIO

from PIL import Image
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from pymongo.connection import Connection
from pymongo import DESCENDING
import gridfs

db = Connection().sms
