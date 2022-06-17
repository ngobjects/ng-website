#!/bin/sh

echo "================== Initiating post_build.sh script =================="

PROJECT_NAME=ng-website
DESTINATION_SERVER=linode-4.rebbi.is
DESTINATION_DIRECTORY=/rebbi/com.fermentedshark/wo/
OLD_APP_NAME=x$PROJECT_NAME`date "+_%Y_%m_%d_%H_%M_%S.woa"`

date "+%Y-%m-%d %H:%M:%S" | tr -d '\n' > $WORKSPACE/target/$PROJECT_NAME.woa/Contents/Resources/buildDate.txt

cd $WORKSPACE

echo "Creating a backup of the remote application"
ssh root@$DESTINATION_SERVER "cp -R $DESTINATION_DIRECTORY$PROJECT_NAME.woa $DESTINATION_DIRECTORY$OLD_APP_NAME"

echo "Transmitting new application to application server"
rsync -avzhe ssh --delete --checksum target/$PROJECT_NAME.woa root@$DESTINATION_SERVER:$DESTINATION_DIRECTORY

echo "================== Finished post_build.sh script =================="
