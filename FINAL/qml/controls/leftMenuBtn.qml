import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15


Button{

    id: btnLeftMenuBtn

    implicitWidth: 250
    implicitHeight: 60

    property url toggleBtnIcon: "../../images/svg/sort-24px.svg"
    property color btnColorDefault: "#1e222a"
    property color btnColorMouseOver: "#23272E"
    property color btnBtnClicked: "#00a1f1"
    property int icon: value
    QtObject{
        id:internal
        property var dynamicColor: if(btnLeftMenuBtn.down){
                                       btnLeftMenuBtn.down ? btnBtnClicked:btnColorDefault
                                   }else{
                                       btnLeftMenuBtn.hovered ? btnColorMouseOver:btnColorDefault
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
            sourceSize.width: 18
            sourceSize.height: 18
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
    D{i:0;autoSize:true;formeditorZoom:0.75;height:40;width:250}
}
##^##*/
