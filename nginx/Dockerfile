FROM nginx:1.25.4-bookworm

COPY conf.d/app.conf /etc/nginx/conf.d/default.conf

EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]