import QtQuick 2.0
import QtQuick.Controls 2.15


Rectangle{


    id: bg
    color: "#4c5568"
    radius: 12
    anchors.fill: parent
    gradient: Gradient {
        GradientStop {
            position: 0
            color: "#4c5568"
        }

        GradientStop {
            position: 1
            color: "#c1cbd5"
        }
    }




    Label {
        id: date
        x: 83
        y: 10
        width: 99
        color: "#c1cbd5"
        text: qsTr("۱۳۹۹/۱۱/۲۲")
        anchors.left: day.right
        anchors.top: parent.top
        anchors.bottom: radilogyPic.top
        horizontalAlignment: Text.AlignLeft
        verticalAlignment: Text.AlignTop
        anchors.topMargin: 10
        anchors.bottomMargin: 20
        anchors.leftMargin: 29
    }

    Image {
        id: radilogyPic
        x: 22
        y: 56
        width: 344
        source: "../../images/test/rad_pic/download.jpg"
        fillMode: Image.PreserveAspectFit
    }

    Label {
        id: day
        x: 8
        y: 10
        color: "#c1cbd5"
        text: qsTr("یکشنبه ")
        anchors.top: parent.top
        anchors.bottom: radilogyPic.top
        anchors.topMargin: 10
        anchors.bottomMargin: 20
    }

    Label {
        id: day1
        x: 538
        y: 10
        color: "#c1cbd5"
        text: qsTr("دکتر امیر جهانشاهی")
        anchors.right: image.left
        anchors.rightMargin: 0
    }

    Image {
        id: image
        x: 692
        y: 8
        width: 100
        height: 100
        anchors.right: parent.right
        source: "../../images/profile/1.jpg"
        anchors.rightMargin: 8
        fillMode: Image.PreserveAspectFit
    }

    Rectangle {
        id: rectangle
        y: 56
        height: 167
        color: "#323f54"
        anchors.left: radilogyPic.right
        anchors.right: parent.right
        anchors.leftMargin: 24
        anchors.rightMargin: 108

        Text {
            id: text1
            color: "#c1cbd5"
            text: qsTr("کشیدن دندان عقل")
            anchors.fill: parent
            font.pixelSize: 12
            anchors.rightMargin: 10
            anchors.leftMargin: 10
            anchors.bottomMargin: 10
            anchors.topMargin: 10
        }
    }





}



/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:800}D{i:6}D{i:10}D{i:9}
}
##^##*/
