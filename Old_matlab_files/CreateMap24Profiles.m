function map = CreateMap24Profiles()

    TonalProfiles;  % get Maj and min global profile variables
    global profileMajRound profileMinRound;
    
    map = NaN(24,12);    
            % create one prototype for each major and each minor profile
    for i=1:12
        map(2*i-1,:) = profileMajRound(i:i+11);
        map(2*i,:) = profileMinRound(i:i+11);
    end   
    
end