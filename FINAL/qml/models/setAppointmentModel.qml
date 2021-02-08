import QtQuick 2.0
import QtQuick.LocalStorage 2.15


Rectangle {
    id: item1
    color: "#4c4e5c"
    radius: 21
    border.color: "#313c4c"
    border.width: 6
    anchors.fill: parent
    property string doc_name_string: "دکتر جهانشاهی"
    Text {
        id: doc_name
        width: 0
        height: 16
        color: "#9edbfe"
        text: doc_name_string
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.topMargin: 20
        anchors.rightMargin: 100
    }

    Text {
        id: time
        width: 0
        height: 16
        color: "#9edbfe"
        text: "18"
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        anchors.bottomMargin: 20
        anchors.rightMargin: 40
    }

    Text {
        id: date
        width: 0
        height: 16
        color: "#9edbfe"
        text: "27/04/137"
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.topMargin: 20
        anchors.leftMargin: 20
    }

    Text {
        id: status
        width: 0
        height: 16
        color: "#9edbfe"
        text: "گذشته"
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        horizontalAlignment: Text.AlignLeft
        verticalAlignment: Text.AlignTop
        anchors.leftMargin: 20
        anchors.bottomMargin: 20
    }
}



/*##^##
Designer {
    D{i:0;autoSize:true;height:100;width:800}
}
##^##*/
