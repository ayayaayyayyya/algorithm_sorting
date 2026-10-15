
function callCloudRunServer() {
  // Cloud Run 배포 후 생성된 URL로 변경
  var url = "https://algorithm-sorting-git-125683312072.europe-west1.run.app"; 
  
  var payload = {
    "data": "Sample data from Google Apps Script"
  };
  
  var options = {
    "method": "post",
    "contentType": "application/json",
    "payload": JSON.stringify(payload)
  };
  
  var response = UrlFetchApp.fetch(url, options);
  Logger.log(response.getContentText());
}
