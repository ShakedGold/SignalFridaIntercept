Java.perform(function () {
    let IncomingTextMessage = Java.use("org.thoughtcrime.securesms.sms.IncomingTextMessage");
    IncomingTextMessage.getMessageBody.overload().implementation = function () {
        let message = this.getMessageBody();
        let sentTimestampMillis = this.getSentTimestampMillis();
  
        send({
          messageText: message,
          timestamp: sentTimestampMillis,
        });
        return message;
    }
});

