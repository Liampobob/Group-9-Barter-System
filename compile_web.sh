mkdir -p mobile/assets/webapp
rm -rf mobile/assets/webapp/*
cd web
npm install
npm run build
cd ..
cp web/dist/* mobile/assets/webapp/
