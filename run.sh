if [ -f "/openedx/config/lms.env.yml.template" ]; then
envsubst < /openedx/config/lms.env.yml.template > /openedx/config/lms.env.yml
fi
if [ -f "/openedx/config/cms.env.yml.template" ]; then
envsubst < /openedx/config/cms.env.yml.template > /openedx/config/cms.env.yml
fi

uwsgi \
    --static-map /static=/openedx/staticfiles/ \
    --static-map /media=/openedx/media/ \
    --http 0.0.0.0:8000 \
    --thunder-lock \
    --single-interpreter \
    --enable-threads \
    --processes=${UWSGI_WORKERS:-2} \
    --buffer-size=8192 \
    --wsgi-file $SERVICE_VARIANT/wsgi.py