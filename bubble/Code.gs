
function callCloudRunServer() {
  // Cloud Run 배포 후 생성된 URL로 변경
  var url = "https://your-cloud-run-service-url.a.run.app/api"; 
  
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
