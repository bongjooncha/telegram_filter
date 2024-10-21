import { useState, useEffect } from "react";
import style from "./index.module.css";
import {
  getAllFilter,
  deleteFilter,
  updateFilter,
  registerChat,
} from "api/filter";

function RunningFilter({
  filter,
  setFilter,
  refresh,
  setRefresh,
  name,
  words,
  trackedRooms,
  receivedRooms,
}) {
  const [filterList, setFilterList] = useState([]);

  useEffect(() => {
    const fetchFilterList = async () => {
      const filters = await getAllFilter();
      setFilterList(filters);
    };
    fetchFilterList();
  }, [refresh]);

  const handleDeleteFilter = async (id) => {
    const confirmDelete = window.confirm("삭제하시겠습니까?");
    if (!confirmDelete) return;
    try {
      await deleteFilter(id);
      setRefresh(!refresh);
      const updatedFilters = filterList.filter((filter) => filter.id !== id);
      setFilterList(updatedFilters);
    } catch (error) {
      console.error("필터 삭제 실패:", error);
    }
  };

  const handleOnOff = async (filter_name) => {
    if (filter_name.on_off === true) {
      const confirmOff = window.confirm(`${name} 필터를 끄시겠습니까?`);
      if (!confirmOff) return;
      const filter_info = {
        filter_name: name,
        tr_id_name: trackedRooms,
        rr_id_name: receivedRooms,
        words: words,
        on_off: false,
      };
      await updateFilter(filter_info);
      setRefresh(!refresh);
    } else {
      const confirmOn = window.confirm(`${name}필터를 작동시키겠습니까?`);
      if (!confirmOn) return;
      const filter_info = {
        filter_name: name,
        tr_id_name: trackedRooms,
        rr_id_name: receivedRooms,
        words: words,
        on_off: true,
      };
      await updateFilter(filter_info);
      await registerChat(filter_info);
      setRefresh(!refresh);
    }
  };

  return (
    <div className={style.RunningFilter}>
      <h1>Running Filter</h1>
      <div className={style.FilterList}>
        {filterList.map((afilter) => (
          <div
            key={afilter.filter_name}
            className={style.FilterItem}
            onClick={() => setFilter(afilter.filter_name)}
          >
            <span
              style={{
                fontWeight: filter === afilter.filter_name ? "bold" : "normal",
                fontStyle: filter === afilter.filter_name ? "italic" : "normal",
              }}
            >
              {afilter.filter_name}
            </span>
            <div className={style.FilterItemButton}>
              <button
                onClick={() => {
                  setFilter(afilter.filter_name);
                  setTimeout(() => {
                    handleOnOff(afilter);
                  }, 100);
                }}
              >
                {afilter.on_off ? "on" : "off"}
              </button>
              <button onClick={() => handleDeleteFilter(afilter.filter_name)}>
                삭제
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default RunningFilter;
