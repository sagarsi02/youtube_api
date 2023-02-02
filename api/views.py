from django.shortcuts import render
from rest_framework.views import APIView
from YoutubeTags import videotags
from rest_framework.response import Response
from rest_framework import status
import logging
from pytube import YouTube


class get_tag(APIView):

    def post(request, *args, **kwargs):
        logging.basicConfig(
            filename="logs/tags.log",
            filemode='a',
            format='%(asctime)s :: >>> %(levelname)s %(message)s',
            datefmt='%H:%M:%S',
            level=logging.INFO
        )

        try:
            body = request.request.data

            if body.get('url'):
                url = body['url']
                youtube_tag = videotags(url)
                if youtube_tag:
                    response = {"Success": f"{youtube_tag}"}
                    logging.info(f"===========================================================================================================")
                    logging.info(f"URL :: >>> {url}")
                    logging.info(f"Tags :: >>> {response}")
                    return Response(response, status=status.HTTP_200_OK)
                else:
                    response = {"Warning": f"No Tags Found"}
                    logging.warning(f"===========================================================================================================")
                    logging.warning(f"URL :: >>> {url}")
                    logging.warning(f"Error :: >>> {response}")
                    return Response(response, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            response = {"Error": f"{e}"}
            logging.error(f"===========================================================================================================")
            logging.error(f"URL :: >>> {url}")
            logging.error(f"Tags :: >>> {response}")
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
