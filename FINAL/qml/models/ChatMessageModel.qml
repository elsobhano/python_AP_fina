import QtQuick 2.0
import QtQuick.LocalStorage 2.15


Rectangle {
    id: item1
    color: "#34363f"
    radius: 21
    border.color: "#313c4c"
    border.width: 6
    anchors.fill: parent
    property string doc_name_string: "دکتر جهانشاهی"
    property string date_string:""
    property string time_string:""
    property string status_string: "گذشته"
    width: 800
    Text {
        id: doc_name
        x: 403
        width: 200
        height: 16
        color: "#9edbfe"
        text: "Dr. Amir Jahanshahi"
        anchors.right: doc_image.left
        anchors.top: parent.top
        horizontalAlignment: Text.AlignRight
        verticalAlignment: Text.AlignVCenter
        anchors.topMargin: 20
        anchors.rightMargin: 57
    }

    Text {
        id: date_and_time
        width: 200
        height: 16
        color: "#9edbfe"
        text: date_string
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.topMargin: 20
        anchors.leftMargin: 20
    }

    Text {
        id: message
        y: 42
        width: 583
        height: 58
        color: "#9edbfe"
        text: "Hello\\nPlease wash your teeth every night"
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        horizontalAlignment: Text.AlignLeft
        verticalAlignment: Text.AlignTop
        wrapMode: Text.WordWrap
        anchors.leftMargin: 20
        anchors.bottomMargin: 20
    }

    Image {
        id: doc_image
        x: 660
        y: 10
        width: 100
        height: 100
        source: "../../../images/rad_images/defaultImage.jpg"
        fillMode: Image.PreserveAspectFit
    }
}
