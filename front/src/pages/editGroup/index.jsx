import { useState, useEffect } from "react";
import style from "./index.module.css";
import { getGroupNames, updateChatGroups, deleteChatGroup } from "api/chat_id";

import Header from "components/Header";
import Name from "components/Name";
import Rooms from "components/Rooms";
import ChatId from "components/ChatIds";

export default function EditGroup() {
  const [name, setName] = useState("");
  const [rooms, setRooms] = useState([]);
  const [groupNames, setGroupNames] = useState([]);
  const [checkedIds, setCheckedIds] = useState([]);
  const [buttonText, setButtonText] = useState("Save");
  const [rerender, setRerender] = useState(false);
  const usage = "editGroup";

  useEffect(() => {
    const fetchGroupNames = async () => {
      try {
        const names = await getGroupNames();
        setGroupNames(names);
      } catch (error) {
        console.error("그룹 이름을 가져오는 데 실패했습니다:", error);
      }
    };
    fetchGroupNames();
  }, []);

  useEffect(() => {
    if (groupNames.includes(name)) {
      if (rooms.length === 0) {
        setButtonText("delete");
      } else {
        setButtonText("edit");
      }
    } else {
      setButtonText("save");
    }
  }, [name, rooms, groupNames]);

  const handleButtonClick = async () => {
    if (buttonText === "delete") {
      await deleteChatGroup(name);
      setRerender((prev) => !prev);
    } else {
      const updatedRooms = rooms.map((room) => ({
        id: room.id,
        name: room.name,
        group: name,
      }));
      setRerender((prev) => !prev);
      try {
        await updateChatGroups(updatedRooms);
        console.log("그룹이 성공적으로 업데이트되었습니다.");
      } catch (error) {
        console.error("그룹 업데이트 중 오류 발생:", error);
      }
    }
  };

  return (
    <div className={style.Main}>
      <Header />
      <div className={style.content}>
        <div className={style.left}>
          <h1>Edit Group</h1>
          <Name designation={"Group Name"} name={name} setName={setName} />
        </div>
        <div className={style.middle}>
          <h2>Rooms</h2>
          <Rooms rooms={rooms} setRooms={setRooms} checkedIds={checkedIds} />
        </div>
        <div className={style.right}>
          <ChatId
            rerender={rerender}
            useage={usage}
            checkedIds={checkedIds}
            setCheckedIds={setCheckedIds}
          />
        </div>
        <div className={style.buttonContainer}>
          <button className={style.button} onClick={handleButtonClick}>
            {buttonText}
          </button>
        </div>
      </div>
    </div>
  );
}
