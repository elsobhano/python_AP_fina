import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15


Button{

    id: btnLeftMenuBtn
    implicitWidth: 250
    implicitHeight: 60

    property url toggleBtnIcon: "../../images/svg/wysiwyg-24px.svg"
    property color btnColorDefault: "#1e222a"
    property color btnColorMouseOver: "#23272E"
    property color btnBtnClicked: "#00a1f1"
    property int iconWidth: 18
    property int iconHeight: 18
    property color fontColor: "#ffffff"
    property color activeColor:"#66686b"
    property color activeColorRight:"#2c313c"
    property bool isActiveMenu: false
    property bool isActiveText: true
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
        anchors.fill: parent
        Rectangle{
            anchors{
                top:parent.top
                left: parent.left
                bottom: parent.bottom

            }
            color: activeColor
            width: 3
            visible: isActiveMenu
        }
        Rectangle{
            anchors{
                top:parent.top
                right: parent.right
                bottom: parent.bottom

            }
            color: activeColorRight
            width: 5
            visible: isActiveMenu
        }
        Image {
            id: iconImg
            width : iconWidth
            height: iconHeight
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            source: toggleBtnIcon
            anchors.leftMargin: 26
            sourceSize.width: iconWidth
            sourceSize.height: iconHeight
            fillMode: Image.PreserveAspectFit

        }
        ColorOverlay{
            source: iconImg
            anchors.fill: iconImg
            color: fontColor

        }

        Text {
            id: textBtnLeftMenu
            color: fontColor
            text: btnLeftMenuBtn.text
            visible: isActiveText
            font: btnLeftMenuBtn.font
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            anchors.leftMargin: 75
        }
    }

}

/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:2;height:60;width:250}
}
##^##*/
