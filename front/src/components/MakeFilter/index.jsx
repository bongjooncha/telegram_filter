import { useState, useEffect } from "react";
import style from "./styles/makeFilter.module.css";
import { updateFilter, getFilter } from "api/filter";

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

  // chossen Filter
  const [filter, setFilter] = useState(null);

  // runfilter component reload
  const [refresh, setRefresh] = useState(false);

  const handleUpdateFilter = async () => {
    if (name.trim() === "") {
      alert("Filter Name is undefined");
      return;
    } else if (trackedRooms.length === 0) {
      alert("Tracked Rooms are undefined");
      return;
    } else if (receivedRooms.length === 0) {
      alert("Received Rooms are undefined");
      return;
    }
    try {
      const formattedTrackedRooms = trackedRooms.map((room) => ({
        id: room.id,
        name: room.name,
      }));
      const formattedReceivedRooms = receivedRooms.map((room) => ({
        id: room.id,
        name: room.name,
      }));
      const filterInfo = {
        filter_name: name,
        tr_id_name: formattedTrackedRooms,
        rr_id_name: formattedReceivedRooms,
        words: words,
      };
      await updateFilter(filterInfo);
    } catch (error) {
      console.error("필터 업데이트 실패:", error);
    } finally {
      console.log("이전 refresh 상태:", refresh);
      setRefresh((prev) => !prev);
      console.log("변경된 refresh 상태:", !refresh);
    }
  };

  useEffect(() => {
    if (filter === null) return;

    const fetchFilter = async (filter) => {
      const filterInfo = await getFilter(filter);
      setName(filterInfo[0].filter_name);
      setWords(filterInfo[0].words);
      setTrackedRooms(filterInfo[0].tr_id_name);
      setReceivedRooms(filterInfo[0].rr_id_name);
    };
    fetchFilter(filter);
  }, [filter]);

  return (
    <div className={style.MakeFilter}>
      <div className={style.contents}>
        <RunningFilter
          filter={filter}
          setFilter={setFilter}
          refresh={refresh}
          setRefresh={setRefresh}
          name={name}
          words={words}
          trackedRooms={trackedRooms}
          receivedRooms={receivedRooms}
        />
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
          <button className={style.compliteButton} onClick={handleUpdateFilter}>
            complite
          </button>
        </div>
      </div>
    </div>
  );
}

export default MakeFilter;
