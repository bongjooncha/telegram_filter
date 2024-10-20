import { useState, useEffect } from "react";
import style from "./index.module.css";
import { getAllFilter, deleteFilter } from "api/filter";

function RunningFilter({ refresh, setRefresh }) {
  const [filterList, setFilterList] = useState([]);

  useEffect(() => {
    const fetchFilterList = async () => {
      const filters = await getAllFilter();
      setFilterList(filters);
    };
    fetchFilterList();
  }, [refresh]);

  const handleDeleteFilter = async (id) => {
    try {
      await deleteFilter(id);
      setRefresh(!refresh);
      const updatedFilters = filterList.filter((filter) => filter.id !== id);
      setFilterList(updatedFilters);
    } catch (error) {
      console.error("필터 삭제 실패:", error);
    }
  };

  return (
    <div className={style.RunningFilter}>
      <h1>Running Filter</h1>
      <div className={style.FilterList}>
        {filterList.map((filter, index) => (
          <div key={filter.filter_name} className={style.FilterItem}>
            <span>{filter.filter_name}</span>
            <button>{filter.on_off ? "on" : "off"}</button>
            <button onClick={() => handleDeleteFilter(filter.filter_name)}>
              삭제
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default RunningFilter;
