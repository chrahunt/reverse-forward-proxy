from nginx:1.17

COPY entrypoint /entrypoint

COPY nginx.conf /etc/nginx/nginx.conf

ENTRYPOINT ["/entrypoint"]

# Full path for nginx otherwise nothing is passed to ENTRYPOINT
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
