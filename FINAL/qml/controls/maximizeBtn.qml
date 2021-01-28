import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15


Button{

    id: btnMaximize

    implicitWidth: 35
    implicitHeight: 35

    property url toggleBtnIcon: "../../images/svg/crop_din-24px.svg"
    property color btnColorDefault: "#1e222a"
    property color btnColorMouseOver: "#23272E"
    property color btnBtnClicked: "#00a1f1"
    QtObject{
        id:internal
        property var dynamicColor: if(btnMaximize.down){
                                       btnMaximize.down ? btnBtnClicked:btnColorDefault
                                   }else{
                                       btnMaximize.hovered ? btnColorMouseOver:btnColorDefault
                                   }
    }

    background: Rectangle{
        id : bgBtn
        color: internal.dynamicColor
        radius: 1
        Image {
            id: iconImg
            width: 16
            height: 15
            anchors.verticalCenter: parent.verticalCenter
            source: toggleBtnIcon
            anchors.horizontalCenterOffset: 0
            anchors.verticalCenterOffset: 2
            anchors.horizontalCenter: parent.horizontalCenter
            fillMode: Image.PreserveAspectFit
        }
        ColorOverlay{
            source: iconImg
            anchors.rightMargin: 0
            anchors.bottomMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 0
            anchors.fill: iconImg
            color: "#ffffff"
        }
    }


}



/*##^##
Designer {
    D{i:0;formeditorZoom:8}
}
##^##*/
