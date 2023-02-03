from django.shortcuts import render
from rest_framework.views import APIView
from YoutubeTags import videotags
from rest_framework.response import Response
from rest_framework import status
import logging
from pytube import YouTube


# Get Youtube Tag
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
                    logging.info(f"URL :: >>> {url}")
                    logging.info(f"Tags :: >>> {response}")
                    return Response(response, status=status.HTTP_200_OK)
                else:
                    response = {"Warning": f"No Tags Found"}
                    logging.warning(f"URL :: >>> {url}")
                    logging.warning(f"Error :: >>> {response}")
                    return Response(response, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            response = {"Error": f"{e}"}
            logging.error(f"URL :: >>> {url}")
            logging.error(f"Tags :: >>> {response}")
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

# Download Youtube Video
class download_video(APIView):

    def post(request, *args, **kwargs):
        logging.basicConfig(
            filename="logs/download_video.log",
            filemode='a',
            format='%(asctime)s :: >>> %(levelname)s %(message)s',
            datefmt='%H:%M:%S',
            level=logging.INFO
        )

        try:
            body = request.request.data

            if body.get('url'):
                url = body['url']
                youtubeObject = YouTube(url)
                youtubeObject = youtubeObject.streams.get_highest_resolution()
                path = "logs/"
                try:
                    youtubeObject.download(path)
                    response = {"Success": f"Successfully Downloaded"}
                    logging.info(f"URL :: >>> {url}")
                    logging.info(f"Download :: >>> {response}")
                    return Response(response, status=status.HTTP_200_OK)
                except Exception as e:
                    response = {"Warning": f"{e}"}
                    logging.warning(f"URL :: >>> {url}")
                    logging.warning(f"Error :: >>> {response}")
                    return Response(response, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            response = {"Error": f"{e}"}
            logging.error(f"URL :: >>> {url}")
            logging.error(f"Tags :: >>> {response}")
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


# View Youtube Video Details
class video_details(APIView):

    def post(request, *args, **kwargs):
        logging.basicConfig(
            filename="logs/video_details.log",
            filemode='a',
            format='%(asctime)s :: >>> %(levelname)s %(message)s',
            datefmt='%H:%M:%S',
            level=logging.INFO
        )

        try:
            body = request.request.data

            if body.get('url'):
                url = body['url']
                youtubeObject = YouTube(url)
                # youtubeObject = youtubeObject.streams.get_highest_resolution()
                try:
                    title = youtubeObject.title
                    desc = youtubeObject.description
                    thumbnail = youtubeObject.thumbnail_url
                    response = {"success": [{"title" : f"{title}", "desc" : f"{desc}", "thumbnail" : f"{thumbnail}" } ]}
                    logging.info(f"URL :: >>> {url}")
                    logging.info(f"Download :: >>> {response}")
                    return Response(response, status=status.HTTP_200_OK)
                except Exception as e:
                    response = {"Warning": f"{e}"}
                    logging.warning(f"URL :: >>> {url}")
                    logging.warning(f"Error :: >>> {response}")
                    return Response(response, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            response = {"Error": f"{e}"}
            logging.error(f"URL :: >>> {url}")
            logging.error(f"Tags :: >>> {response}")
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
