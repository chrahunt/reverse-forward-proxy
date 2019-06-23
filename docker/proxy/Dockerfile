FROM reiz/nginx_proxy:latest

COPY nginx.conf /usr/local/nginx/conf/nginx.conf

# Use exec form so it propagates signals correctly.
CMD ["/usr/local/nginx/sbin/nginx"]
