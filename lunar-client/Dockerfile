FROM node:alpine as build
COPY . /build
WORKDIR /build
RUN npm i && npm run build

FROM nginx:stable
COPY --from=build /build/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
