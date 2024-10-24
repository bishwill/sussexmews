deploy-website:
	aws s3 sync src s3://bishop-industries-eu-west-2-sussexmews-website-files \
	--delete \
	--exclude "*" \
	--include "*.html" \
	--include "*.jpg"