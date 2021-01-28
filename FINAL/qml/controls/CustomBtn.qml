import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15


Button{

    id: btnToggle

    implicitWidth: 70
    implicitHeight: 60

    property url toggleBtnIcon: "../../images/svg/sort-24px.svg"
    property color btnColorDefault: "#1e222a"
    property color btnColorMouseOver: "#23272E"
    property color btnBtnClicked: "#00a1f1"
    QtObject{
        id:internal
        property var dynamicColor: if(btnToggle.down){
                                       btnToggle.down ? btnBtnClicked:btnColorDefault
                                   }else{
                                       btnToggle.hovered ? btnColorMouseOver:btnColorDefault
                                   }
    }

    background: Rectangle{
        id : bgBtn
        color: internal.dynamicColor
        radius: 1
        Image {
            id: iconImg
            width : 25
            height: 25
            anchors.verticalCenter: parent.verticalCenter
            source: toggleBtnIcon
            anchors.horizontalCenter: parent.horizontalCenter
            fillMode: Image.PreserveAspectFit
        }
        ColorOverlay{
            anchors.fill: iconImg
            source: iconImg
            color: "#ffffff"
            antialiasing: false
        }
    }

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:40;width:200}
}
##^##*/
