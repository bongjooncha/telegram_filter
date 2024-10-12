import { useState } from "react";
import style from "./styles/makeFilter.module.css";

import RunningFilter from "./RunningFilter";
import Name from "components/Name";
import WordLists from "./WordLists";
import Rooms from "components/Rooms";
import ChatId from "components/ChatIds";

function MakeFilter() {
  //  name
  const [name, setName] = useState("");
  //items
  const [activeSection, setActiveSection] = useState("words");
  // choose words
  const [words, setWords] = useState([]);
  // trackedroom
  const [trackedRooms, setTrackedRooms] = useState([]);
  // recivedroom
  const [receivedRooms, setReceivedRooms] = useState([]);
  // chating rooms
  const [checkedIds, setCheckedIds] = useState([]);

  return (
    <div className={style.MakeFilter}>
      <div className={style.contents}>
        <RunningFilter />
        <div className={style.items}>
          <div className={style.Name}>
            <Name designation={"Filter Name"} name={name} setName={setName} />
          </div>
          <div className={style.itemsHeader}>
            <div
              onClick={() => setActiveSection("words")}
              className={
                activeSection === "words" ? style.activate : style.deactivate
              }
            >
              choose words
            </div>
            <div
              onClick={() => setActiveSection("tracked")}
              className={
                activeSection === "tracked" ? style.activate : style.deactivate
              }
            >
              tracked room
            </div>
            <div
              onClick={() => setActiveSection("received")}
              className={
                activeSection === "received" ? style.activate : style.deactivate
              }
            >
              received room
            </div>
          </div>
          <div>
            {activeSection === "words" && ( // 수정: activeSection에 따라 WordLists 렌더링
              <WordLists words={words} setWords={setWords} />
            )}
            {activeSection === "tracked" && ( // 수정: activeSection에 따라 trackedRooms 렌더링
              <Rooms
                rooms={trackedRooms}
                setRooms={setTrackedRooms}
                checkedIds={checkedIds}
              />
            )}
            {activeSection === "received" && ( // 수정: activeSection에 따라 receivedRooms 렌더링
              <Rooms
                rooms={receivedRooms}
                setRooms={setReceivedRooms}
                checkedIds={checkedIds}
              />
            )}
          </div>
        </div>
        <div className={style.chatrooms}>
          <ChatId checkedIds={checkedIds} setCheckedIds={setCheckedIds} />
        </div>
        <div className={style.compButPa}>
          <button className={style.compliteButton}>complite</button>
        </div>
      </div>
    </div>
  );
}

export default MakeFilter;
